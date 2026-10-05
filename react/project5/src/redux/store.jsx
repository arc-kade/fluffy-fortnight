import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "./counterslice"
import counter from "../components/counter";
export const store = configureStore({
    reducer:{
        counter:counterReducer
    }
})