function Button(props) {
    return (
        <button className={`btn ${props.type}`} onClick={props.onClick}>
            {props.label}
        </button>
    )
}
export default Button;