import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="This program launches restG4 jobs to slurm. Values in brackets [] are optional"
    )
    parser.add_argument("-c", "--config", metavar="RML_FILE", required=True)
    parser.add_argument("-n", "--section-name", default="",
                        help="Defines the name of the section to be used from RML_FILE")
    parser.add_argument("-e", "--email", default="",
                        help="It allows to specify the e-mail for batch system job notifications")
    # parser.add_argument("-i", "--initialRun", metavar="VALUE", help="An integer number to introduce the first run number.")
    parser.add_argument("-i", "--id-offset", default=0, type=int)
    parser.add_argument("-r", "--repeat", metavar="REPEAT_VALUE", type=int, default=10,
                        help="This option defines the number of simulations we will launch (default is 10)")
    parser.add_argument("-d", "--delay", metavar="DELAY_TIME", type=int, default=30,
                        help="Time delay between launching 2 reapeated jobs (default is 30 seconds)")
    parser.add_argument("-j", "--job-name", metavar="JOB_NAME", default="",
                        help="JOB_NAME defines the name of scripts and output files stored under slurmJobs/")

    parser.add_argument("-o", "--only-scripts", action="store_true",
                        help="It will just generate the slurm scripts without launching to the queue")
    parser.add_argument("-l", "--log-path", default="", help="log output directory")
    return parser


def main():
    args = create_parser().parse_args()
    return 0

if __name__ == '__main__':
    main()