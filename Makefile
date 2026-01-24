PY?=python3
PELICAN?=.venv/bin/pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

DEBUG ?= 0
ifelse($(DEBUG), 1, PELICANOPTS += -D)

BUCKET=fintech-monster-regional
PROJECT_ID=fintechmonster
URL_MAP=fintech-monster-lb

help: ## Show this help
	@echo 'Makefile for Fintech Monster'
	@echo ''
	@echo 'Usage:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

html: ## (re)generate the web site
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean: ## remove the generated files
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate: ## regenerate files upon modification
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve: ## serve site at http://localhost:8000
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

dev: ## start auto-reloading development server
	$(PELICAN) -l -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

devserver: dev ## alias for dev


deploy: publish ## build and deploy to Google Cloud Storage
	gcloud --project $(PROJECT_ID) storage rsync -r --delete-unmatched-destination-objects $(OUTPUTDIR) gs://$(BUCKET)
	# Set HTML to revalidate every time
	gcloud --project $(PROJECT_ID) storage objects update gs://$(BUCKET)/**/*.html --cache-control="public, no-cache, proxy-revalidate"
	# Set assets to cache for 1 hour (ignore errors if no assets found)
	-gcloud --project $(PROJECT_ID) storage objects update gs://$(BUCKET)/theme/** gs://$(BUCKET)/images/** --cache-control="public, max-age=3600"

nocache: ## set zero cache for everything (debug only)
	gcloud --project $(PROJECT_ID) storage objects update gs://$(BUCKET)/** --cache-control="public, max-age=0, no-store"

invalidate: ## invalidate Cloud CDN cache
	gcloud compute url-maps invalidate-cdn-cache $(URL_MAP) --path "/*" --project $(PROJECT_ID)

.PHONY: html help clean regenerate serve publish deploy invalidate nocache
