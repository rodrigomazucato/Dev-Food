import { useNavigate } from "react-router-dom";
import { useState } from "react";
import Button from "../componentes/Button";
import Input from "../componentes/Input";

function Forms() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const navigate = useNavigate();

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
    console.log('oie')
    localStorage.setItem("nomeUsuario", nome);
    localStorage.setItem("nomeEmail", email);

    if (validarCampos()) {
      navigate("/Cadastro");
    }
  }

  return (
    <div className="space-y-4 p-8 bg-white rounded-md shadow flex flex-col m-6 w-100 h-100">
      <Input nome={nome} setNome={setNome} email={email} setEmail={setEmail} />

      <Button variant="filled" onClick={handleSubmit} >
        Continuar
      </Button>
    </div>
  );
}

export default Forms;
