#include <iostream>
#include <string>
#include <fstream>
#include "../dependencies/CLI11.hpp"
#include <filesystem>

namespace fs = std::filesystem;

void searchFiles(std::string path){
    for(auto it = fs::recursive_directory_iterator(path); it != fs::recursive_directory_iterator(); ++it)
    {
        const auto& entry = *it;
        if (entry.is_directory() && entry.path().filename() == "__pycache__")
        {
            it.disable_recursion_pending();
            continue;
        }
        if (entry.is_regular_file())
        {
            std::cout << entry.path().string() << '\n';
        }
    }
}

int main(int argc, char *argv[]){
    CLI::App coreParser{"An argument parser for Protus Core"};

    auto list = coreParser.add_subcommand("list", "A subcommand to list things on the project");

    bool payloads = false;
    bool modules = false;

    list->add_flag("--payloads", payloads, "An option for list command to show the payloads");
    list->add_flag("--modules", modules, "An option for list command to show the current modules");

    auto general = coreParser.add_subcommand("protus", "A general subcommand");

    bool protus_info = false;

    general->add_flag("--info", protus_info, "It shows the information about Protus Framework Remake");

    CLI11_PARSE(coreParser, argc, argv);

    if (payloads)
    {
        std::cout << "Listing payloads...\n";
        searchFiles("payloads");
    }
    else if (modules)
    {
        std::cout << "Listing modules...\n";
        searchFiles("modules");
    }
    else if (protus_info)
    {
        std::cout << "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"; 
        std::cout << "Protus, The Pentest Framework - REMAKE\n";
        std::cout << "Version - 0.1.4v\n";
        std::cout << "Description: Protus, The Framework for Pentest is a tool to assist offensive cybersecurity engineers in their work\n";
        std::cout << "Developed by RetroGuy1336\n";
    }
}
