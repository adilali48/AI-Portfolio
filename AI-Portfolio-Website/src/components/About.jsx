function About() {
  return (
    <section
      id="about"
      className="bg-slate-900 text-white py-24 px-8"
    >
      <div className="max-w-6xl mx-auto">

        <h2 className="text-5xl font-bold text-center mb-12">
          About <span className="text-cyan-400">Me</span>
        </h2>

        <div className="bg-slate-800 rounded-2xl p-10 shadow-xl">

          <p className="text-lg text-gray-300 leading-8">
            Hi! I'm <span className="text-cyan-400 font-semibold">Adil Ali</span>,
            an aspiring AI & Python Developer from Pakistan.
          </p>

          <p className="mt-6 text-lg text-gray-300 leading-8">
            I enjoy building real-world AI applications using Python,
            Streamlit, React, Google Gemini AI, and modern AI tools.
          </p>

          <p className="mt-6 text-lg text-gray-300 leading-8">
            My goal is to become a professional AI Engineer and Freelance
            AI Developer by creating practical AI solutions that solve
            real-world problems.
          </p>

          <div className="grid md:grid-cols-3 gap-6 mt-12">

            <div className="bg-slate-700 rounded-xl p-6 text-center">
              <h3 className="text-4xl font-bold text-cyan-400">10+</h3>
              <p className="mt-2">AI Projects</p>
            </div>

            <div className="bg-slate-700 rounded-xl p-6 text-center">
              <h3 className="text-4xl font-bold text-cyan-400">Python</h3>
              <p className="mt-2">Main Programming Language</p>
            </div>

            <div className="bg-slate-700 rounded-xl p-6 text-center">
              <h3 className="text-4xl font-bold text-cyan-400">2026</h3>
              <p className="mt-2">Building AI Portfolio</p>
            </div>

          </div>

        </div>

      </div>
    </section>
  );
}

export default About;