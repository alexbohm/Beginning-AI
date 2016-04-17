#include <iostream>
#include <vector>
using namespace std;
class Link;
class Word {
public:
	string type, word; int links_iterator;
	Link *out_links[10];
	Word(string worde, string typee) {
		word = worde;
		type = typee;
		links_iterator = 0;
	}
	Word(){ word = ""; type = ""; }
	void add_link(Link, vector<Link> all_links);
};
class Link {
public:
	Word node1, node2; float charge_reduc;
	Link(Word one, Word two, vector<Link> all_links, int charge_red=1) {
		node1 = one; node2 = two;
		charge_reduc = charge_red;
		all_links.push_back(*this);
	}
	Link(){}
};
void Word::add_link(Link lk, vector<Link> all_links) {*out_links[links_iterator] = lk; links_iterator++;}

class Network : public Link, Word {
	int default_charge; vector<Link> *all_links; //don't forget * for all_links if used locally
	Network(vector<Link> all_link, int defchg=10) {
		all_links = &all_link;
		default_charge = defchg;
	}
};



int main() {
	vector<Link> all_links;
	/*melon
	grape*/
}
