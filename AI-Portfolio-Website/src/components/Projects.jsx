function Projects() {
  const projects = [
    {
      title: "Gemini AI Chatbot",
      description: "AI chatbot built with Python, Streamlit and Google Gemini AI.",
    },
    {
      title: "AI PDF Chatbot",
      description: "Chat with PDF documents using Google Gemini AI.",
    },
    {
      title: "AI Resume Analyzer",
      description: "Analyze resumes and provide AI-powered feedback.",
    },
    {
      title: "AI Email Generator",
      description: "Generate professional emails instantly using AI.",
    },
    {
      title: "AI YouTube Summarizer",
      description: "Summarize YouTube videos using AI.",
    },
    {
      title: "Python Calculator",
      description: "Simple calculator built with Python.",
    },
  ];

  return (
    <section id="projects" className="bg-slate-900 text-white py-24 px-8">
      <div className="max-w-7xl mx-auto">

        <h2 className="text-5xl font-bold text-center mb-14">
          My <span className="text-cyan-400">Projects</span>
        </h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">

          {projects.map((project, index) => (
            <div
              key={index}
              className="bg-slate-800 rounded-2xl p-6 shadow-lg hover:scale-105 transition"
            >
              <h3 className="text-2xl font-bold text-cyan-400 mb-4">
                {project.title}
              </h3>

              <p className="text-gray-300 mb-6">
                {project.description}
              </p>

              <div className="flex gap-4">
                <button className="bg-cyan-500 px-4 py-2 rounded-lg hover:bg-cyan-600">
                  GitHub
                </button>

                <button className="border border-cyan-400 px-4 py-2 rounded-lg hover:bg-cyan-500 hover:text-black">
                  Live Demo
                </button>
              </div>
            </div>
          ))}

        </div>

      </div>
    </section>
  );
}

export default Projects;