const API_URL = 'http://localhost:8000'

export const translate = async (text: string, src: string) => {
  const dest = src === 'es' ? 'gn' : 'es'

  console.log(text, src, dest)

  try {
    const url = `${API_URL}/translate?text=${text}&source=${src}&target=${dest}`

    const response = await fetch(url)
    const data = await response.json()

    return data.translation
  } catch (error) {
    throw new Error((error as Error).message)
  }
}
