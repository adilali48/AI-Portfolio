import {
  FaPython,
  FaReact,
  FaGithub,
  FaGitAlt,
} from "react-icons/fa";

import {
  SiStreamlit,
  SiGoogle,
  SiMysql,
} from "react-icons/si";

function Skills() {
  const skills = [
    { name: "Python", icon: <FaPython size={50} className="text-yellow-400" /> },
    { name: "React", icon: <FaReact size={50} className="text-cyan-400" /> },
    { name: "Streamlit", icon: <SiStreamlit size={50} className="text-red-400" /> },
    { name: "Gemini AI", icon: <SiGoogle size={50} className="text-blue-400" /> },
    { name: "Git", icon: <FaGitAlt size={50} className="text-orange-500" /> },
    { name: "GitHub", icon: <FaGithub size={50} className="text-white" /> },
    { name: "SQL", icon: <SiMysql size={50} className="text-blue-500" /> },
  ];

  return (
    <section
      id="skills"
      className="bg-slate-950 text-white py-24 px-8"
    >
      <div className="max-w-7xl mx-auto">

        <h2 className="text-5xl font-bold text-center mb-14">
          My <span className="text-cyan-400">Skills</span>
        </h2>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-8">

          {skills.map((skill, index) => (
            <div
              key={index}
              className="bg-slate-800 rounded-2xl p-8 text-center hover:scale-105 duration-300 shadow-lg"
            >
              <div className="flex justify-center mb-4">
                {skill.icon}
              </div>

              <h3 className="text-xl font-semibold">
                {skill.name}
              </h3>
            </div>
          ))}

        </div>

      </div>
    </section>
  );
}

export default Skills;