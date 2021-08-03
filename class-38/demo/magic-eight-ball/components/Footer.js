import Link from 'next/link'
import React from 'react'


// export default function Footer(props){
//     return(
//         <footer className="bg-red-400 text-gray-100 p-4 items-center">
//         <Link href="/careers">
//             <a>Careers</a>
//         </Link>
//         </footer>
//     )
// }

export default class Footer extends React.Component{

    constructor(){
        super();
        this.state = {
            x: 1
        };
    }

    render(){
        return(
            <footer className="bg-red-400 text-gray-100 p-4 items-center">
                <Link href="/careers">
                    <a>Careers</a>
                </Link>
            </footer>
        )
    }

}