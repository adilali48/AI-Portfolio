import { FaEnvelope, FaGithub, FaLinkedin } from "react-icons/fa";

function Contact() {
  return (
    <section
      id="contact"
      className="bg-slate-950 text-white py-24 px-8"
    >
      <div className="max-w-6xl mx-auto text-center">

        <h2 className="text-5xl font-bold mb-10">
          Contact <span className="text-cyan-400">Me</span>
        </h2>

        <p className="text-gray-400 text-lg mb-12">
          Interested in working together? Feel free to contact me.
        </p>

        <div className="grid md:grid-cols-3 gap-8">

          {/* Email */}
          <div className="bg-slate-800 p-8 rounded-2xl shadow-lg hover:scale-105 transition duration-300">
            <FaEnvelope className="text-5xl text-cyan-400 mx-auto mb-4" />

            <h3 className="text-2xl font-bold mb-3">
              Email
            </h3>

            <a
              href="mailto:aliadilrajper11@gmail.com"
              className="text-gray-300 hover:text-cyan-400"
            >
              aliadilrajper11@gmail.com
            </a>
          </div>

          {/* GitHub */}
          <div className="bg-slate-800 p-8 rounded-2xl shadow-lg hover:scale-105 transition duration-300">
            <FaGithub className="text-5xl text-cyan-400 mx-auto mb-4" />

            <h3 className="text-2xl font-bold mb-3">
              GitHub
            </h3>

            <a
              href="https://github.com/adilali48"
              target="_blank"
              rel="noopener noreferrer"
              className="text-gray-300 hover:text-cyan-400"
            >
              github.com/adilali48
            </a>
          </div>

          {/* LinkedIn */}
          <div className="bg-slate-800 p-8 rounded-2xl shadow-lg hover:scale-105 transition duration-300">
            <FaLinkedin className="text-5xl text-cyan-400 mx-auto mb-4" />

            <h3 className="text-2xl font-bold mb-3">
              LinkedIn
            </h3>

            <a
              href="https://linkedin.com/in/adil-ali-a28989285"
              target="_blank"
              rel="noopener noreferrer"
              className="text-gray-300 hover:text-cyan-400"
            >
              linkedin.com/in/adil-ali-a28989285
            </a>
          </div>

        </div>

      </div>
    </section>
  );
}

export default Contact;