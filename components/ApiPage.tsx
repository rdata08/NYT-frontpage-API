"use client"
import React from 'react'
import { VanishInput } from './ui/VanishInput'

export default function ApiPage (){
    const pass = () => {
        
    }

    return (
        <div className='flex justify-center relative my-20 z-10 pb-20 pt-36'>
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
        </div>
    )
}