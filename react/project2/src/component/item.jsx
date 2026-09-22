function item(){
    const items = ["apple","banana","orange","strawberry"]
    const students = [
        {id:1,name:"Abilash"},
        {id:2,name:"Shaun"},
        {id:3,name:"John Doe"},
        {id:4,name:"Ram"},
        {id:5,name:"Avdol"}
    ]
    return(
        <>
        <ul>
            {items.map(item=>(
                <li key={item}>{item}</li>
            ))}
        </ul>
        <ol>
            {students.map(student=>(
                <li key={student.id}>{student.name}</li>
            ))}
        </ol>
        </>
    )
}
export default item;