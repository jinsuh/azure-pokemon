package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	resp, err := http.Get("http://pokemondb.net/pokedex/all")
	
	if err != nil {
		fmt.Println("ERRORORORORORORO")
	}
	body, err := ioutil.ReadAll(resp.Body)
	resp.Body.Close()
	if err != nil {
		fmt.Println("ERRORORORO LATER ON")
	}
	fmt.Printf("%s", body)
	
}
