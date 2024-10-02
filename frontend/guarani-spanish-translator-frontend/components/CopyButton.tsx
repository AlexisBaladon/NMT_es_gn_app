'use client'

import Image from 'next/image'
import React, { useState } from 'react'

interface CopyButtonProps {
  textToCopy: string
}

function CopyButton({ textToCopy }: CopyButtonProps) {
  const [copied, setCopied] = useState(false)

  const copyToClipboard = async () => {
    if (!textToCopy) return console.error('No text to copy')

    if (navigator.clipboard) {
      try {
        await navigator.clipboard.writeText(textToCopy)
        setCopied(true)
        setTimeout(() => setCopied(false), 2000) // Reset the copied state after 2 seconds
      } catch (err) {
        console.error('Failed to copy: ', err)
      }
    } else {
      console.error('Clipboard API is not available')
    }
  }

  return (
    <button
      className={`p-2 rounded-full transition-colors ${textToCopy && 'hover:bg-gray-100'}`}
      onClick={copyToClipboard}
      disabled={!textToCopy}
    >
      <Image
        src={copied ? '/icons/check.svg' : '/icons/copy.svg'}
        height={24}
        width={24}
        alt="Copy to Clipboard"
      />
    </button>
  )
}

export default CopyButton
