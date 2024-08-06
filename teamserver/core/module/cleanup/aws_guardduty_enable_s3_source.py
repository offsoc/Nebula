import sys

author = {
    "name":"gl4ssesbo1",
    "twitter":"https://twitter.com/gl4ssesbo1",
    "github":"https://github.com/gl4ssesbo1",
    "blog":"https://www.pepperclipp.com/"
}

needs_creds = True

variables = {
	"SERVICE": {
		"value": "guardduty",
		"required": "true",
        "description":"The service that will be used to run the module. It cannot be changed."
	},
	"DETECTOR-ID": {
		"value": "",
		"required": "true",
        "description":"The ID of the GuardDuty Detector to Disable"
	}
}
description = "Reenabled Guard Duty Data Sources that has been disabled before"

aws_command = "aws guardduty update-detector --detector-id <detector-id>  --enable  --region <region> --profile <profile>"

calls = [
	"guardduty:UpdateDetector"
]

def exploit(profile, workspace):
	detectorID = variables['DETECTOR-ID']['value']

	try:
		profile.update_detector(
			DetectorId=detectorID,
			DataSources={
				'S3Logs': {
					'Enable': True
				}
			}
		)
		status = f"Detector {detectorID} S3 Source was enabled"
	except Exception as e:
		status = f"Detector {detectorID} S3 Source was not enabled with error code: {str(e)}."

	return {
		"Detector": {
			"Detector": detectorID,
			"Status": status
		}
	}


