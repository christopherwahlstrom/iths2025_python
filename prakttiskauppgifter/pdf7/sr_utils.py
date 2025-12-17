def print_channels(channels_list):
    if not channels_list:
        print("Inga kanaler hittade.")
        return
    
    print(f"\nHittade {len(channels_list)} kanaler:\n")


    for channel in channels_list:
       name = channel.get("name")
       tagline = channel.get("tagline", "Ingen beskrivning tillgänglig")

       print(f"---{name}---")
       print(f"Info: {tagline}\n")
       print("-" * 20)

