import Input from "../componentes/Input";
import { useState } from "react";
import Button from "../componentes/Button";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const navigate = useNavigate();

  function botaoCadastro() {
    navigate("/Cadastro");
  }
  function botaoContinuar() {
    navigate("/home");
  }

  return (
    <div className="w-screen h-screen bg-red-100 flex flex-col items-center p-6">
      <h1 className="text-3xl text-stone-950 font-bold text-center">
        Faça o seu login
      </h1>

      <form className="space-y-4 p-8 !mt-[3rem] bg-white rounded-md shadow flex flex-col w-100">
        <legend className="text-center"> Como deseja continuar?</legend>
        <div>
          <Input
            label="Informe o seu nome:"
            id="nome"
            type="text"
            value={nome}
            placeholder={"Fulando de tal"}
            onChange={setNome}
          />
          <Input
            label="Informe o seu email:"
            id="email"
            type="email"
            value={email}
            placeholder={"fulando@exemplo.com"}
            onChange={setEmail}
          />
        </div>

        <div className="flex justify-end">
          <span className="text-gray-medio"> Não tem conta?</span>
          <Button variant="plain" onClick={botaoCadastro}>
            Cadastre-se!
          </Button>
        </div>

        <Button variant="filled" onClick={botaoContinuar}>
          Continuar
        </Button>

        <span className="text-center text-gray-medio mt-4">
          -------------- OU --------------
        </span>

        <Button
          variant="filledIcon"
          color="secundary"
          img
          onClick={botaoContinuar}
        >
          Fazer login com o Google
        </Button>
      </form>
    </div>
  );
}
