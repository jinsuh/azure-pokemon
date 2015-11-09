function updateTextInput(isAttacker, val) {
	if (isAttacker) {
		document.getElementById('attacker-level').value=val; 	
	}
	else {
		document.getElementById('defender-level').value=val; 		
	}
      
}