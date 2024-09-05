"use client"
import React from 'react'
import { VanishInput } from './ui/VanishInput'
import { CodeBlock, dracula } from 'react-code-blocks';

export default function ApiPage() {
    const pass = () => {

    }

    const code = `
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
                    onChange={pass}
                    onSubmit={pass}
                />
            </div>
            <CodeBlock 
            text = {code}
            />
        </div>
    )
}