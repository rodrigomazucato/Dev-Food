import Forms from "./pages/Forms";

function App() {
  return (
    <div className="w-screen h-screen bg-red-100 flex flex-col items-center p-6">
      <h1 className="text-3xl text-stone-950 font-bold text-center">
        Cadastre-se
      </h1>
      <Forms />
    </div>
  );
}
export default App;
