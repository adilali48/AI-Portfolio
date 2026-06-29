import { Link } from "react-scroll";

function Navbar() {
  return (
    <nav className="fixed top-0 left-0 w-full bg-slate-900/90 backdrop-blur-md text-white shadow-lg z-50">
      <div className="max-w-7xl mx-auto flex justify-between items-center px-8 py-5">
        <h1 className="text-3xl font-bold text-cyan-400">
          Adil<span className="text-white">AI</span>
        </h1>

        <ul className="hidden md:flex gap-8 text-lg">
          <li>
            <Link to="home" smooth={true} duration={500} className="cursor-pointer hover:text-cyan-400">
              Home
            </Link>
          </li>

          <li>
            <Link to="about" smooth={true} duration={500} className="cursor-pointer hover:text-cyan-400">
              About
            </Link>
          </li>

          <li>
            <Link to="projects" smooth={true} duration={500} className="cursor-pointer hover:text-cyan-400">
              Projects
            </Link>
          </li>

          <li>
            <Link to="contact" smooth={true} duration={500} className="cursor-pointer hover:text-cyan-400">
              Contact
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;