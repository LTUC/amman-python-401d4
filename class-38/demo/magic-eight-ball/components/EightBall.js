export default function EightBall(props){
    return(
      <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
          <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-200 top-16 left-16">
              {/* Use the state "reply" */}    
              <p className="text-xl text-center">{props.getMostRecentReply()}</p>
          </div>
      </div>
    );
  }