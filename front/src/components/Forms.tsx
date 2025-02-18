function Forms() {
  return (
    <div className="space-y-4 p-6 bg-white rounded-md shadow flex flex-col m-6">
      <input
        type="text"
        placeholder="Digite o seu nome"
        className="border border-slate-300 outline-slate-400 px-4 py-2 rounded-md"
      ></input>

      <input
        type="text"
        placeholder="Digite o seu email"
        className="border border-slate-300 outline-slate-400 px-4 py-2 rounded-md"
      ></input>
    </div>
  );
}

export default Forms;
