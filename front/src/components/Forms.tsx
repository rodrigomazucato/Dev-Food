import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Forms() {
  const navigate = useNavigate();

  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");

  const validarCampos = (): boolean => {
    const nomeTrim = nome.trim();
    const emailTrim = email.trim();

    if (nomeTrim === "" || emailTrim === "") {
      alert("Preencha todos os campos!");
      return false;
    }

    return true;
  };

  function handleSubmit() {
    localStorage.setItem("nomeUsuario", nome);
    localStorage.setItem("nomeEmail", email);

    if (validarCampos()) {
      navigate("/Cadastro");
    }
  }

  return (
    <div className="space-y-4 p-6 bg-white rounded-md shadow flex flex-col m-6 w-100 h-100">
      <h1 className="text-3xl text-center text-stone-800 font-bold">
        Falta pouco para matar sua fome!
      </h1>
      <h1 className="font-medium text-stone-700">Informe o seu nome</h1>
      <input
        type="text"
        id="nome"
        name="nome"
        placeholder="Digite o seu nome"
        className="border border-slate-300 outline-slate-400 px-4 py-2 rounded-md"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      ></input>
      <h1 className="font-medium text-stone-700">Informe o seu e-mail</h1>
      <input
        type="text"
        id="email"
        name="email"
        placeholder="Digite o seu e-mail"
        className="border border-slate-300 outline-slate-400 px-4 py-2 rounded-md"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      ></input>
      <button
        onClick={handleSubmit}
        className="font-medium text-white bg-red-600 rounded-md p-2 cursor-pointer"
      >
        Continuar
      </button>
    </div>
  );
}

export default Forms;
