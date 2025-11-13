package main


import (
"encoding/json"
"log"
"net/http"
"time"
"github.com/example/aurora/grader/pkg/sandbox"
)


type RunRequest struct{
Language string `json:"language"`
Code string `json:"code"`
Tests map[string]string `json:"tests"`
}


func runHandler(w http.ResponseWriter, r *http.Request){
var req RunRequest
if err := json.NewDecoder(r.Body).Decode(&req); err != nil{
http.Error(w, "bad request", 400)
return
}


ctx, cancel := context.WithTimeout(context.Background(), 20*time.Second)
defer cancel()


result, err := sandbox.Run(ctx, req.Language, req.Code, req.Tests)
if err != nil{
http.Error(w, err.Error(), 500)
return
}
json.NewEncoder(w).Encode(result)
}


func main(){
http.HandleFunc("/run", runHandler)
log.Println("grader listening on :8080")
http.ListenAndServe(":8080", nil)
}
