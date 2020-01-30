function f_options() { 
	var options = document.getElementById("options");
	var item = options.options[options.selectedIndex].text;
	console.log(item)

	if (item == "Jerusalem") {
		document.getElementById("paragraphs").innerHTML=
		"1) Studio pnima <br> 072-2513336 <br> <br> 2) Sivananda Yoga Center Jerusalem <br> 02-6714854 <br> <br> 3) camellia Yoga Center <br> 077-2313077 <br> <br> 4) Saara Jahkola Yoga <br> 054-5575717 <br> <br> 5) Vijnana Yoga <br> 077-4243494"
	}

	else if (item == "Tel-Aviv") {
		document.getElementById("paragraphs").innerHTML= "1) Chandra Yoga Tel Aviv <br> 03-546-4045 <br> <br> 2) Prana Yoga College <br> 03-629-6661 <br> <br> 3) Yoga Levontin <br> 03-560-3888 <br> <br> 4) orhayoga <br> 03-525-5052 <br> <br> 5) Bikram Yoga Israel <br> 03-624-1807"
	} 


	else if (item == "Haifa") {
		document.getElementById("paragraphs").innerHTML= "1) Yoga Laya <br> 050-693-0827 <br> <br> 2) ONE-YOGA <br> 054-572-9715 <br> <br> 3) YogAdi <br> 052-888-8303 <br> <br> 4) Studio Naim Haifa <br> 03-518-8998 <br> <br> 5) HaStudio <br> 058-761-6363"
	} 


	else if (item == "Beersheba") {
		document.getElementById("paragraphs").innerHTML= "1) livyoga <br> 054-220-3771 <br> <br> 2) Yoga Beersheba <br> <br> 3) Studio Positive <br> 08-647-2340 <br> <br> 4) TET ATET <br> 050-779-1774 <br> <br> 5) My Way <br> 054-593-1945"
	}


	else if (item == "Eilat") {
		document.getElementById("paragraphs").innerHTML= "1) Eilat Yoga House <br> 052-819-8626 <br> <br> 2) Yoga Eilat Studio <br> 03-237-4837 <br> <br> 3) Sivananda Eilat <br> 03-696-1810"
	} 

	document.getElementById("choose a city").style.display = "none";
}


