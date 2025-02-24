interface InputProps {
  nome: string;
  setNome: (value: string) => void;
  email: string;
  setEmail: (value: string) => void;
}

export default function Input({ nome, setNome, email, setEmail }: InputProps) {
  return (
    <div>
      <h1 className="text-center font-bold">
        Falta pouco para matar sua fome!
      </h1>
      <div className="flex flex-col mb-4">
        <label htmlFor="nome" className="font-medium text-stone-700 mb-1">
          Informe o seu nome:
        </label>
        <input
          type="text"
          id="nome"
          name="nome"
          placeholder="Digite o seu nome"
          className="border border-slate-300 outline-slate-400 px-4 py-2 rounded-md"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        ></input>
      </div>

      <div className="flex flex-col">
        <label htmlFor="email" className="font-medium text-stone-700 mb-1">
          Informe o seu e-mail:
        </label>
        <input
          type="text"
          id="email"
          name="email"
          placeholder="Digite o seu e-mail"
          className="border border-slate-300 outline-slate-400 px-4 py-2 rounded-md"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        ></input>
      </div>
    </div>
  );
}
