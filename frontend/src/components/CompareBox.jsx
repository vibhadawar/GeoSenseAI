function CompareBox() {
  return (
    <section
      id="compare"
      className="py-20"
    >
      <div className="bg-white rounded-2xl shadow-lg p-8">

        <h2 className="text-3xl font-bold mb-8">
          Compare Satellite Images
        </h2>

        <div className="grid md:grid-cols-2 gap-6">

          <div>
            <label>Image A</label>

            <input
              type="file"
              className="w-full border p-3 rounded-lg"
            />
          </div>

          <div>
            <label>Image B</label>

            <input
              type="file"
              className="w-full border p-3 rounded-lg"
            />
          </div>

        </div>

        <button
          className="mt-6 bg-green-600 text-white px-6 py-3 rounded-lg"
        >
          Compare Images
        </button>

        <div className="mt-8 p-6 bg-slate-100 rounded-lg">

          <h3 className="font-semibold text-lg">
            Change Detection
          </h3>

          <p className="mt-2">
            Change Percentage: 14%
          </p>

        </div>

      </div>
    </section>
  );
}

export default CompareBox;