import { useNavigate } from "react-router-dom";
import Button from "./Button";

export default function FormLogin() {
  const navigate = useNavigate();

  function handleSubmit() {
    navigate("/home");
  }

  return (
    <div className="space-y-4 p-8 mt-30 bg-white rounded-md shadow flex flex-col w-100">
      <legend className="text-center">Como deseja continuar?</legend>

      <Button variant="filled" onClick={handleSubmit}>
        Login
      </Button>

      <legend className="text-center">Ou</legend>

      <Button img={true} variant="filled" onClick={handleSubmit}>
        Entrar com Google
      </Button>
    </div>
  );
}
