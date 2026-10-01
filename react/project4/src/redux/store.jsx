import {createStore} from "redux";
import reducer from "./reducer";
import { createStoreHook } from "react-redux";

const store = createStore(reducer)
export default store