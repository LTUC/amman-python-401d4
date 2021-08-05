import { useState } from "react";

export default function LoginForm(props){

    function submitHandler(event){
        event.preventDefault();
        console.log(event.target.username.value, event.target.password.value);
        props.loginHandler({username:username, password:password})

    }

    const [username, setUsername] = useState('');
    function usernameChangeHandler(event){
        event.preventDefault();
        console.log('username',event.target.value);
        setUsername(event.target.value);
    }

    const [password, setPassword] = useState('');
    function passwordChangeHandler(event){
        event.preventDefault();
        console.log('password',event.target.value);
        setPassword(event.target.value);
    }

    return(
        <form className="flex flex-col w-1/2 gap-4 p-8 mx-auto my-4 text-center bg-gray-200 border-2 border-gray-400 rounded-lg text-md" onSubmit={submitHandler}>
            <div className="flex flex-col ">
                <label className="mb-2 font-bold uppercase text-grey-darkest" htmlFor="username">User Name</label>
                <input className="px-3 py-2 border text-grey-darkest" type="text" name="username" id="username" placeholder="User Name" onChange={usernameChangeHandler} />
            </div>

            <div className="flex flex-col ">
                <label className="mb-2 font-bold uppercase text-grey-darkest" htmlFor="password">Password</label>
                <input className="px-3 py-2 border text-grey-darkest" type="password" name="password" id="password" placeholder="password" onChange={passwordChangeHandler}/>
            </div>

            <button className="px-3 py-4 mt-8 uppercase bg-gray-500 rounded text-green hover:bg-gray-600 text-gray-50" type="submit">Sign In</button>

        </form>
    )
}