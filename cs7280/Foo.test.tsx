import { render } from '@testing-library/react';
import Foo from './Foo';

test('renders foo', () => {
  const { container } = render(<Foo label="one" />);
  expect(container).toMatchSnapshot();
});
