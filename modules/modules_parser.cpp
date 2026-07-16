#include <iostream>
#include <fstream>
#include <string>
#include "../dependencies/CLI11.hpp"
#include "../dependencies/json.hpp"

struct scanArgs 
{
    std::string host;
    int first_port = 0;
    int last_port = 0;
    int time = 0;
    std::string show =  "all";
};

using json = nlohmann::json;

int json_Scan(const scanArgs& args){
    json Communication;
    Communication["host"] = args.host;
    Communication["first_port"] = args.first_port;
    Communication["last_port"] = args.last_port;
    Communication["time"] = (args.time < 1 ? 0 : args.time);

    if (args.show == "open" || args.show == "filtered" || args.show == "unknown")
    {
        Communication["show"] = args.show;
    }

    else if (!args.show.empty())
    {
        Communication["show"] = "all";
    }

    std::ofstream file("communication.json");

    if (file.is_open())
    {
        file << Communication.dump();

        file.close();
        return 0;
    }

    else
    {
        std::cout << "ERROR! Cannot open the json file!\n";

        return -1;
    }
}

int json_Look(std::string domain)
{
    json Communication;
    Communication["domain"] = domain;

    std::ofstream file("communication.json");

    if (file.is_open())
    {
        file << Communication.dump();

        file.close();

        return 0;
    }

    else
    {
        std::cout << "ERROR! Cannot open the json file!\n";

        return -1;
    }
}

int json_Finder(std::string domain, int speed)
{
    json Communication;
    Communication["domain"] = domain;

    if (speed != 0)
    {
        Communication["speed"] = speed;
    }

    std::ofstream file("communication.json");

    if (file.is_open())
    {
        file << Communication.dump();

        file.close();

        return 0;
    }

    else
    {
        std::cout << "ERROR! Cannot open the json file!\n";

        return -1;
    }
}

int main(int argc, char *argv[]) {
    CLI::App modulesParser{"An argument parser for Protus Modules"};

    modulesParser.require_subcommand(1);

    auto scan = modulesParser.add_subcommand("scan", "Scans a host");

    std::string host;
    int port = 0;
    int time = 0;
    std::string show;

    scan->add_option("host", host, "Host to scan")->required();
    scan->add_option("-p,--port", port, "port")->required();
    scan->add_option("-t,--time", time, "time to scan");
    scan->add_option("--show", show, "Show only open ports");

    auto look = modulesParser.add_subcommand("look", "It performs a DNS lookup on the host.");

    std::string domain;

    look->add_option("domain", domain, "Domain to be consulted")->required();

    auto find = modulesParser.add_subcommand("find", "Find subdomains of the primary domain.");

    std::string findDomain;
    int speed = 0;

    find->add_option("domain", findDomain, "Domain to be tested.")->required();
    find->add_option("-s", speed);

    CLI11_PARSE(modulesParser, argc, argv);

    if (*scan)
    {
        scanArgs args;
        args.host       = host;   // cópia da variável simples para a struct
        args.first_port = 0;
        args.last_port  = port;
        args.time       = time;
        args.show       = (show == "open" || show == "filtered" || show == "unknown")
                        ? show : "all";

        return json_Scan(args);
    }

    else if (*look)
    {
        return json_Look(domain);
    }

    else if (*find)
    {
        return json_Finder(findDomain, speed);
    }

    return 0;
}
