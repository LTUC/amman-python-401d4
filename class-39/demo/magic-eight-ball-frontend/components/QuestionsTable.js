export default function QuestionsTable(props){
    return(
      <table className="w=1/2 mx-auto my-4">
        <thead>
          <tr>
            <th className="border border-blue-600">No.</th>
            <th className="border border-blue-600">Quesiton</th>
            <th className="border border-blue-600">Response</th>
          </tr>
        </thead>
        <tbody>
          {
            props.answeredQuestions.map(item => {
              return(
                <tr>
                  <td className="border border-blue-600">{item.id}</td>
                  <td className="border border-blue-600">{item.question}</td>
                  <td className="border border-blue-600">{item.reply}</td>
                </tr>
              )
            })
          }
          
        </tbody>
      </table>
    );
  }