import readme from "../../readme.md?raw";

export interface Content {
  id: string;
  title: string;
  img: string;
}

export const parseContents = (): Content[] => {
  const REGEX = /^##\s+\d+\.\s+(.*)/gm;

  const matches = readme.match(REGEX);
  if (!matches) return [];

  return matches.map((match: string): Content => {
    const id = match.substring(4, 7);
    const title = match.substring(9).trim();
    const img = `img/${id}.png`;
    return { id, title, img };
  });
};

export const filterContent = (keyword: string) => {
  return ({ title }: Content) => {
    return title.toLowerCase().includes(keyword.toLowerCase());
  };
};
