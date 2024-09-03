"use client"
import MagicButton from './ui/MagicButton'
import { Spotlight } from './ui/Spotlight'
import { TextGenerateEffect } from './ui/TextGenerateEffect'
import { FaLock } from 'react-icons/fa6'
import { useRouter } from '@/node_modules/next/navigation'

export default function Hero() {
    const router = useRouter();

    const goToApiPage = () => {
        router.push("/api");
    };

    return (
        <div className='pb-20 pt-36'>

            <div className='flex justify-center relative my-20 z-10'>
                <div className='max-w-[89w] md:max-w-2xl lg:max-w-[60vw] flex flex-col items-center justify-center'>
                    <TextGenerateEffect
                        className="text-center text-[40px] md:text-5xl, lg:text-6xl font-noto-serif-georgian"
                        words="The New York Times Front Page API"
                    />

                    <p className='text-center md:tracking-wider mb-4 text-sm md:text-lg lg:text-2xl'>
                        Welcome! This API utilizes OAuth 2.0 for authorization.
                    </p>

                    <MagicButton
                        title="Authorize"
                        icon={<FaLock />}
                        position='right'
                        handleClick={goToApiPage}
                    />
                </div>
            </div>
        </div>

    )
}