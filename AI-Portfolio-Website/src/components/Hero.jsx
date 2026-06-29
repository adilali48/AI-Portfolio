import { TypeAnimation } from "react-type-animation";
import profile from "../assets/profile.png";

function Hero() {
  return (
    <section
      id="home"
      className="min-h-screen bg-slate-950 text-white flex items-center justify-center px-8 pt-24"
    >
      <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">

        {/* Left Side */}
        <div>
          <h3 className="text-cyan-400 text-xl mb-3">
            👋 Welcome to My Portfolio
          </h3>

          <h1 className="text-6xl font-bold leading-tight">
            Hi, I'm <span className="text-cyan-400">Adil Ali</span>
          </h1>

          <div className="text-3xl font-semibold mt-6 text-gray-300">
            <TypeAnimation
              sequence={[
                "AI Engineer",
                2000,
                "Python Developer",
                2000,
                "Machine Learning Enthusiast",
                2000,
                "Generative AI Developer",
                2000,
              ]}
              wrapper="span"
              speed={50}
              repeat={Infinity}
            />
          </div>

          <p className="mt-8 text-lg text-gray-400 max-w-xl">
            Passionate about building AI-powered applications using
            Python, React, Streamlit, LangChain, RAG and Google Gemini AI.
          </p>

          <div className="mt-10 flex gap-5">
            <button className="bg-cyan-500 hover:bg-cyan-600 px-7 py-3 rounded-xl font-semibold transition">
              View Projects
            </button>

            <a
              href="/resume.pdf"
              target="_blank"
              rel="noopener noreferrer"
              className="border border-cyan-400 px-7 py-3 rounded-xl hover:bg-cyan-500 hover:text-black transition"
            >
              Download Resume
            </a>
          </div>
        </div>

        {/* Right Side */}
        <div className="flex justify-center">
          <img
            src={profile}
            alt="Adil Ali"
            className="w-80 h-80 rounded-full object-cover border-4 border-cyan-400 shadow-2xl"
          />
        </div>

      </div>
    </section>
  );
}

export default Hero;