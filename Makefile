.PHONY: all build run clean package

all: build

build:
	@chmod +x build.sh run.sh
	@./build.sh

run: build
	@./run.sh

clean:
	@echo "Cleaning up..."
	@rm -f /data/cloudshop.db
	@rm -f cloudshop.tar.gz cloudshop.zip

package:
	@echo "Packaging source tree with git history..."
	@git archive --format=tar.gz --output=cloudshop.tar.gz HEAD
	@git archive --format=zip --output=cloudshop.zip HEAD
