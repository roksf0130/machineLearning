from collections import defaultdict
from collections import OrderedDict

# 존재하지 않는 키값을 참조하는 경우 에러 발생
# d = dict()
# print(d["first"])

# defaultdict 는 존재하지 않는 키값을 참조하면 기본값을 리턴
d = defaultdict(object)     # Default dictionary를 생성
d = defaultdict(lambda : 0)  # Default 값을 0으로 설정합
print(d["first"])

text = """A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them. Talk about low-hanging fruit!
What's more, press releases are cost effective. If the release results in an article that (for instance) appears to recommend your firm or your product, that article is more likely to drive prospects to contact you than a comparable paid advertisement.
However, most press releases never accomplish that. Most press releases are just spray and pray. Nobody reads them, least of all the reporters and editors for whom they're intended. Worst case, a badly-written press release simply makes your firm look clueless and stupid.
For example, a while back I received a press release containing the following sentence: "Release 6.0 doubles the level of functionality available, providing organizations of all sizes with a fast-to-deploy, highly robust, and easy-to-use solution to better acquire, retain, and serve customers."
Translation: "The new release does more stuff." Why the extra verbiage? As I explained in the post "Why Marketers Speak Biz Blab", the BS words are simply a way to try to make something unimportant seem important. And, let's face it, a 6.0 release of a product probably isn't all that important.
As a reporter, my immediate response to that press release was that it's not important because it expended an entire sentence saying absolutely nothing. And I assumed (probably rightly) that the company's marketing team was a bunch of idiots.""".lower().split()

print(text)

# dict 를 사용하여 단어 빈도수를 확인하는 로직
# 키값의 존재여부를 확인하여 존재하면 빈도수 증가, 존재하지 않으면 신규 엘리먼트를 생성
word_count = {}
for word in text:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# defaultdict 를 사용하면 키값의 존재여부를 체크할 필요 없음
word_count = defaultdict(object)     # Default dictionary를 생성
word_count = defaultdict(lambda: 0)  # Default 값을 0으로 설정합
for word in text:
    word_count[word] += 1
for i, v in OrderedDict(sorted(word_count.items(), key = lambda t : t[1], reverse=True)).items():
    print(i, v)
