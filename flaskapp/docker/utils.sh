# Printer with shell colors
function utils.printer {
	# BASH COLORS
	GREEN=`tput setaf 2`
	RESET=`tput sgr0`
	if [[ ! -z "$2" ]]; then
		# print new line before
    	echo ""
    fi
    echo -e "${GREEN}$1${RESET}"
}  


# Create enviroment files if don't exists
function utils.check_envs_files {
	ENV_FILES=("$@")
	for i in "${ENV_FILES[@]}";  do
		if [[ ! -f "$i" ]]; then
			cp "$i.example" "$i"
		fi
	done
}


# Load environment vars in root directory
function utils.load_environment {
	if [[ ! -z $(cat envs | xargs)  ]]; then
	    # export $(grep -vwE "#" envs | xargs) 
	    set -a
		source envs     
		set +a
	fi
}

# Load meteor settings var enviroment
function utils.load_environment_prod {
	# Set build tag
	export SERVICE_METEOR_BUILD_TAG_CALC=${SERVICE_METEOR_BUILD_TAG}-latest
	if [[ ! -z "${BUILD_NUMBER}" ]]; then
		sed -i /SERVICE_METEOR_BUILD_NUMBER/c\SERVICE_METEOR_BUILD_NUMBER=${BUILD_NUMBER} envs
		export BUILD_NUMBER_CALC=${BUILD_NUMBER}
		if [[ ! -z "${SERVICE_METEOR_BUILD_AMOUNT}" ]]; then
			export BUILD_NUMBER_CALC=$((${BUILD_NUMBER}%${SERVICE_METEOR_BUILD_AMOUNT}))
	    fi
	    export SERVICE_METEOR_BUILD_TAG_CALC=${SERVICE_METEOR_BUILD_TAG}-${BUILD_NUMBER_CALC}
	else [[ ! -z "${SERVICE_METEOR_BUILD_NUMBER}" ]]
		export BUILD_NUMBER_CALC=${SERVICE_METEOR_BUILD_NUMBER}
		if [[ ! -z "${SERVICE_METEOR_BUILD_AMOUNT}" ]]; then
			export BUILD_NUMBER_CALC=$((${SERVICE_METEOR_BUILD_NUMBER}%${SERVICE_METEOR_BUILD_AMOUNT}))
	    fi
	    export SERVICE_METEOR_BUILD_TAG_CALC=${SERVICE_METEOR_BUILD_TAG}-${BUILD_NUMBER_CALC}
	fi

	# Set prefix for push and pull images from dockerhub
	if [[ -z "${DOCKERHUB_ORGANIZATION}" ]]; then
	    export DOCKERHUB_PREFIX=${DOCKERHUB_USER}
	else
	    export DOCKERHUB_PREFIX=${DOCKERHUB_ORGANIZATION}
	fi
}

# Load environment vars in root directory
function utils.current_folder_name {
	echo $(pwd | grep -o '[^/]*$') | tr "[:upper:]" "[:lower:]"
}


# Copy meteor files to build context
function utils.copy_meteor_build_files {
	BUILD_FILES=(${SERVICE_METEOR_BUILD_COPY_FILES//,/ })
	for i in "${BUILD_FILES[@]}";  do
		echo "$i"
	    if [[ -f "$i" ]]; then
	        cp "$i" "../${SERVICE_METEOR_BUILD_CONTEXT}/$i"
	    else
	        touch "$i"
	        cp "$i" "../${SERVICE_METEOR_BUILD_CONTEXT}/$i"
	    fi
	done
}

