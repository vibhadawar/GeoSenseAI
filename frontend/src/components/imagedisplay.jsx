function ImageDisplay() {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <h2 className="text-2xl font-bold mb-6">
        Image Results
      </h2>

      <div className="grid md:grid-cols-2 gap-6">

        <div>

          <h3 className="font-semibold mb-3">
            Original Image
          </h3>

          <img
            src="https://placehold.co/600x400"
            alt="Original"
            className="rounded-xl w-full"
          />

        </div>

        <div>

          <h3 className="font-semibold mb-3">
            Segmented Image
          </h3>

          <img
            src="https://placehold.co/600x400"
            alt="Segmented"
            className="rounded-xl w-full"
          />

        </div>

      </div>

    </div>
  );
}

export default ImageDisplay;