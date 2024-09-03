import Hero from "@/components/Hero";
import React from "react";

export default function Home() {
    return (
        <main className="relative flex justify-center items-center flex-col overflow-hidden mx-auto sm:px-10 px-5 min-h-[100vh]">
            <video src="/videos/videoBg.mp4"
            autoPlay
            loop
            muted
            className="absolute top-0 left-0 w-full h-[100vh] object-cover z-0"
            />
            
            <div className="max-w-7xl w-full">
                <Hero/>
            </div>
        </main>
    )
}

