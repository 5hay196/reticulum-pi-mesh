package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

// rnsSharedInstancePort is the default port the Python RNS shared instance listens on.
const rnsSharedInstancePort = 37428

func main() {
	fmt.Println("[Integration] Reticulum Pi Mesh - Go integration layer")
	fmt.Printf("[Integration] Will connect to RNS shared instance on localhost:%d\n", rnsSharedInstancePort)

	// TODO: Implement the RNS shared instance protocol to:
	//   - Register destinations
	//   - Send and receive packets
	//   - Listen for announcements
	// Ref: https://reticulum.network/manual/reference.html

	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	fmt.Println("[Integration] Running. Ctrl+C to stop.")
	<-quit
	fmt.Println("[Integration] Shutting down.")
}
