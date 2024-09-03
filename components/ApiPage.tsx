"use client"
import React from 'react'
import { VanishInput } from './ui/VanishInput'

export default function ApiPage (){
    const pass = () => {
        
    }

    return (
        <div className='pb-20 pt-36'>
            <h1>Api Page</h1>
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