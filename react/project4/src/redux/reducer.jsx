const initialState={
    count:0,
    message:"Hello redux"
}
function reducer(state=initialState,action){
    switch(action.type){
        case "INCREAMENT":
            return{
                ...state,
                count: state.count + 1
            }
        case "DECREAMENT":
            return{
                ...state,
                count: state.count - 1
            }
        case "SET_MESSAGE":
            return{
                ...state,
                message: action.payload
            }
        default: return state
    }
}
export default reducer;