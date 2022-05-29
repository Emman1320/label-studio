import React from "react";
import { useState } from "react";
import 'ToggleButton.css';


const ToggleButton = ({ label }) => {
	const [isChecked, setisChecked]=useState(false);
	const displayPage=(e)=>{
		if(e===true){
			return <Page/>
		}
	}
	return (
		<>
		<div className="container">
	{label}{" "}
	<div className="toggle-switch">
		<input type="checkbox" className="checkbox"
			name={label} id={label} onChange={()=>{setisChecked(!isChecked)}}/>
		<label className="label" htmlFor={label}>
		<span className="inner" />
		<span className="switch" />
		</label>
	</div>
	</div>
	{displayPage(isChecked)}
	
		</>
	
);
};

export default ToggleButton;
