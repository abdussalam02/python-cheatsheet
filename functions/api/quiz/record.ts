/// <reference path="../../types.d.ts" />

const SUPPORTED_LOCALES = ['en', 'zh', 'es', 'fr', 'de', 'ja', 'ru', 'ko', 'pt'] as const

/**
 * Normalize path to English version by removing language prefix
 * This ensures all language versions of the same page share the same quiz data
 */
function normalizePathToEnglish(path: string): string {
  const segments = path.split('/').filter(Boolean)
  if (segments.length > 0 && SUPPORTED_LOCALES.includes(segments[0] as typeof SUPPORTED_LOCALES[number])) {
    segments.shift()
    return segments.length > 0 ? '/' + segments.join('/') : '/'
  }
  return path
}

export async function onRequestPost(context: {
  request: Request
  env: {
    PYTHONCHEATSHEET_QUIZ_KV: KVNamespace
  }
}): Promise<Response> {
  try {
    const { request, env } = context

    // Validate request method
    if (request.method !== 'POST') {
      return new Response(
        JSON.stringify({ error: 'Method not allowed' }),
        {
          status: 405,
          headers: { 'Content-Type': 'application/json' },
        }
      )
    }

    // Parse request body
    const body = await request.json()
    const { quizId, pagePath } = body

    // Validate required fields
    if (!quizId || !pagePath) {
      return new Response(
        JSON.stringify({ error: 'Missing required fields: quizId and pagePath' }),
        {
          status: 400,
          headers: { 'Content-Type': 'application/json' },
        }
      )
    }

    // Normalize path to English version to ensure all languages share the same quiz data
    const normalizedPath = normalizePathToEnglish(pagePath)
    // Generate unique key: combine normalized pagePath and quizId
    const key = `quiz:${normalizedPath}:${quizId}`

    // Get current count from KV
    const currentCount = await env.PYTHONCHEATSHEET_QUIZ_KV.get(key)
    const count = currentCount ? parseInt(currentCount, 10) : 0

    // Increment count
    const newCount = count + 1

    // Save to KV
    await env.PYTHONCHEATSHEET_QUIZ_KV.put(key, newCount.toString())

    // Return success response
    return new Response(
      JSON.stringify({
        success: true,
        quizId,
        pagePath: normalizedPath,
        count: newCount,
      }),
      {
        status: 200,
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type',
          // POST 请求不缓存
          'Cache-Control': 'no-store, no-cache, must-revalidate',
        },
      }
    )
  } catch (error) {
    console.error('Error recording quiz completion:', error)
    return new Response(
      JSON.stringify({ error: 'Internal server error' }),
      {
        status: 500,
        headers: {
          'Content-Type': 'application/json',
          'Cache-Control': 'no-store, no-cache, must-revalidate',
        },
      }
    )
  }
}

export async function onRequestOptions(): Promise<Response> {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  })
}

