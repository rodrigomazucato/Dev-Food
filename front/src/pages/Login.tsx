import FormLogin from "../componentes/FormLogin";

export default function Login() {
  return (
    <div className="w-screen h-screen bg-red-100 flex flex-col items-center p-6">
      <h1 className="text-3xl text-stone-950 font-bold text-center">
        Faça o seu login
      </h1>

      <FormLogin />
    </div>
  );
}
