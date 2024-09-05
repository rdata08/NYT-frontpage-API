"use client"
import React from 'react'
import { VanishInput } from './ui/VanishInput'
import { CodeBlock, dracula } from 'react-code-blocks';
import { useState } from 'react';

export default function ApiPage() {
    const[inputValue, setInputValue] = useState('')

    const handleChange = (event) => {
       setInputValue(event.target.value);
    }

    const handleSubmit = async (event) => {
        event.preventDefault()
        try {
            const response = await fetch()
        }
    }

    const response = `
    Hello!
    `;

    return (
        <div className='flex flex-col justify-center items-center relative my-20 z-10 pb-20 pt-36'>
            <h1>NYT API</h1>
            <div>
                <VanishInput
                    placeholders={[
                        "Placeholder",
                        "Placeholder 2",
                        "Placeholder 3"
                    ]}
                    onChange={handleChange}
                    onSubmit={handleSubmit}
                />
            </div>
            <div className='w-full h-screen'>
                <CodeBlock
                    text={response}
                    language="json"
                    showLineNumbers={false}
                    theme={dracula}
                    wrapLines={true}
                />
            </div>
        </div>
    )
}