
function Navbar() {
  return (
    <nav className="bg-slate-900 text-white px-6 py-4">
      <div className="max-w-7xl mx-auto flex justify-between items-center">

        <h1 className="text-2xl font-bold text-green-400">
          GeoSense AI
        </h1>

        <div className="hidden md:flex gap-8">
          <a href="#home">Home</a>
          <a href="#features">Features</a>
          <a href="#analysis">Analysis</a>
          <a href="#compare">Compare</a>
          <a href="#about">About</a>
        </div>

        <button className="bg-green-500 px-4 py-2 rounded-lg">
          Get Started
        </button>

      </div>
    </nav>
  );
}

export default Navbar;